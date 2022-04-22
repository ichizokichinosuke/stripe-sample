import os
import json
import stripe

from dotenv import load_dotenv, find_dotenv
from flask import Flask, redirect, render_template, request, jsonify

# Setup Stripe python client library
load_dotenv(find_dotenv())

app = Flask(__name__)

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.route("/")
def checkout():
    return render_template('checkout.html')

@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/create-checkout-session", methods=["POST"])
def create_checkout_session():
    price_id = request.form.get('priceId')
    session = stripe.checkout.Session.create(
        line_items=[{
            "price": price_id,
            "quantity": 1,
        }],
        mode="subscription",
        success_url="http://localhost:4242/success",
        cancel_url='http://localhost:4242/cancel',
    )
    return redirect(session.url, code=303)

@app.route('/webhook', methods=['POST'])
def webhook_received():
    webhook_secret = os.getenv("STRIPE_WEBHOOK_SECRET")
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    if event_type == 'checkout.session.completed':
    # Payment is successful and the subscription is created.
    # You should provision the subscription and save the customer ID to your database.
      print(data)
    elif event_type == 'invoice.paid':
    # Continue to provision the subscription as payments continue to be made.
    # Store the status in your database and check when a user accesses your service.
    # This approach helps you avoid hitting rate limits.
      print(data)
    elif event_type == 'invoice.payment_failed':
    # The payment failed or the customer does not have a valid payment method.
    # The subscription becomes past_due. Notify your customer and send them to the
    # customer portal to update their payment information.
      print(data)
    else:
      print('Unhandled event type {}'.format(event_type))

    return jsonify({'status': 'success'})

@app.route('/customer-portal', methods=['POST'])
def customer_portal():
    # For demonstration purposes, we're using the Checkout session to retrieve the customer ID.
    # Typically this is stored alongside the authenticated user in your database.
    checkout_session_id = request.form.get('sessionId')

    checkout_session = stripe.checkout.Session.retrieve(checkout_session_id)

    # This is the URL to which the customer will be redirected after they are
    # done managing their billing with the portal.
    return_url = "http://localhost:4242/",

    session = stripe.billing_portal.Session.create(
        customer=checkout_session.customer,
        return_url=return_url,
    )
    return redirect(session.url, code=303)



if __name__ == "__main__":
    app.run(port=4242)
