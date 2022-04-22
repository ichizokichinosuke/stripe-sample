# stripeのサンプルコード
- built_checkout: 構築済みのStripeCheckoutを利用した都度決済のサンプルコード

- subscription: 構築済みのStripe Checkoutを利用したサブスクリプションのサンプルコード
### 公式ドキュメント
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout
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
1. /templates/checkout.htmlのinputタグのvalueを取得したAPI IDに置き換える
1. cd subscription
1. python server.py
1. http://localhost:4242 へアクセス

## テスト
- テストカード情報を使用して支払い情報を入力
    - カード番号として 4242 4242 4242 4242 を入力
    - カードの有効期限として任意の将来の日付を入力
    - 任意の 3 桁のセキュリティーコードを入力
    - 請求先の任意の郵便番号を入力
- 支払う をクリック
- 新しい成功ページにリダイレクトされる

### テスト詳細
[公式ドキュメント](https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout#%E3%83%86%E3%82%B9%E3%83%88%E3%81%99%E3%82%8B)
## Reference
https://stripe.com/docs/payments/accept-a-payment?platform=web&ui=checkout

https://stripe.com/docs/billing/subscriptions/build-subscriptions