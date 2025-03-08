# Stripe Promotion Code Generator
#### Video Demo:  <[URL HERE](https://youtu.be/EorBaIAYRBg)>
#### Description:
The **Stripe Promotion Code Generator** is a command-line interface tool to help *non-technical* individuals to bulk generate promotion codes in Stripe.
##### How does it work
**Step 1:** Users provide their own API key from Stripe to connect their Stripe account. No data is stored while using the program.

**Step 2:** Set up a coupon by answering a couple of questions related to:
- The type of your coupon (forever, once, repeating)
- The percentage of discount
- Option: the duration of your coupon for coupons of the type "repeating"

**Step 3:** Generate promotion codes for the newly created coupon. Simply define:
- How many promotion codes you want to generate
- The redemption limit of every coupon code (minimum 1)

**Output:** Once all codes are generated, you will be able to see these live in Stripe under 'Project Catalog > Coupon'. Click on the newly created coupon to find the codes.

You will also have a file available on **your device** that contains a .csv with your coupon and it's codes to make it easier to use the promotion codes to upload on external software (Klaviyo, Mailchimp, WooCommerce, etc.)

##### Software considerations
The software is relatively bloated and could be rewritten to perform faster and use less memory. All code is in subsequent steps with a lot of validation going on. Potentially moving things into a class would have been a better approach but I steered away from this given the use of Stripe's API.

##### Community next steps:
- There are multiple other settings possible for the coupon and the promotion codes that are not included in this program. Others can continue expanding the code base with additional validations and variables based on Stripe's documentation for [Coupon Codes](https://docs.stripe.com/api/coupons/create) and [Promotion Codes](https://docs.stripe.com/api/promotion_codes/create).
- There are multiple other manipulations possible with coupons and promotion codes such as *updating, retrieving and deleting* that are not part of this initial program.
- The API key validation is too simple, essentially allowing any key starting with sk_, pk_ or rk_ to be accepted. I am unsure how I can test if an API key is valid before having the user run through the whole program. Keep in mind I never touched Python until 3 months ago - I would love to learn from someone how to validate or authenticate the API key.

##### License
MIT License
Copyright (c) 2025 Jeroen De Koninck
