# stripeのサンプルコード
- built_checkout: 構築済みのStripeCheckoutを利用した都度決済のサンプルコード

- subscription: 構築済みのStripe Checkoutを利用したサブスクリプションのサンプルコード

## Prerequisite
Python3.6以上の実行環境

## Stripe上の共通設定
1. Stripeダッシュボードで[アカウント名](https://dashboard.stripe.com/settings/account/)が設定されていることを確認
1. Stripeダッシュボードで[シークレットキー](https://dashboard.stripe.com/test/apikeys)の取得

## ローカルでの共通設定
1. .envファイルを作成
1. STRIPE_SECRET_KEYに取得したシークレットキーをコピー

## build_checkout
1. cd build_checkout
1. python server.py
1. http://localhost:4242 へアクセス
## subscrition
1. [Stripeダッシュボード](https://dashboard.stripe.com/test/products?active=true)で商品の作成
1. API IDを取得
1.
## Reference
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout

https://stripe.com/docs/billing/subscriptions/build-subscriptions