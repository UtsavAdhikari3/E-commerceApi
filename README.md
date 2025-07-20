## 🧠 SYSTEM LAYOUT FOR AN E-COMMERCE API

---

### 1. **Users**

Handles authentication, registration, and customer profiles.

* **User** (provided by Django's `AbstractUser`)

  * username, email, password, is\_staff (admin), etc.
* **CustomerProfile**

  * user (OneToOne)
  * phone, address, city, country, etc.

🔸 **Auth Requirements**:

* Register
* Login (token or JWT)
* View/Update Profile
* Admin users manage the store

---

### 2. **Products**

These are what users browse, search, and buy.

* **Product**

  * name, description, price, category, image, stock, is\_active
* **Category**

  * name, slug, description (optional)
* **Brand** (optional)

  * name, logo

🔸 **Features**:

* View all products
* Search by name, category, brand
* Filter by price range, availability
* Admins can CRUD products

---

### 3. **Cart System**

Temporary place to hold products before purchase.

* **Cart**

  * user (nullable or tied to session for anonymous carts)
  * created\_at
* **CartItem**

  * cart (FK)
  * product (FK)
  * quantity

🔸 **Features**:

* Add item to cart
* Remove item from cart
* View current cart
* Change quantity

---

### 4. **Orders**

Tracks completed purchases.

* **Order**

  * user, created\_at, total\_price, status (e.g. pending, shipped, delivered)
  * shipping\_address
  * payment\_status
* **OrderItem**

  * order
  * product
  * quantity
  * price\_at\_purchase (for historical accuracy)

🔸 **Flow**:

* On checkout: convert Cart → Order
* Deduct product stock
* Send confirmation
* Admin can manage order status

---

### 5. **Payment Integration**

You won’t store credit card details yourself.

* Integrate with:

  * Stripe
  * PayPal
  * Razorpay (for Asia)
* Store only minimal transaction details:

  * **Payment**

    * order (FK), amount, provider, transaction\_id, status

🔸 Flow:

* User clicks "Pay"
* Call payment gateway
* Confirm success
* Mark `Order.payment_status = "paid"`

---

### 6. **Wishlist / Favorites (Optional)**

Let users save items.

* **Wishlist**

  * user
  * products (many-to-many)

---

### 7. **Reviews & Ratings (Optional)**

Enhances product credibility.

* **Review**

  * user, product, rating, comment, created\_at

---

### 8. **Admin Panel (Optional API or Django Admin)**

* Manage products, orders, users
* View analytics
* Add inventory

---

## 🔁 Relationships (Quick Summary)

```text
User ───┬─▶ CustomerProfile
        ├─▶ Cart ───┬─▶ CartItem ──▶ Product
        ├─▶ Order ──┬─▶ OrderItem ──▶ Product
        └─▶ Wishlist (M2M) ──▶ Product

Product ─▶ Category
        └─▶ Brand

Order ──▶ Payment
```

---

## 🔍 Key Features to Build

| Feature         | API Endpoint Examples            |
| --------------- | -------------------------------- |
| Browse Products | `/api/products/`                 |
| View Product    | `/api/products/<id>/`            |
| Search Products | `/api/products/?search=keyboard` |
| User Signup     | `/api/auth/register/`            |
| Login           | `/api/auth/login/`               |
| View Cart       | `/api/cart/`                     |
| Add to Cart     | `/api/cart/add/`                 |
| Checkout        | `/api/checkout/`                 |
| Make Payment    | `/api/payment/`                  |
| View Orders     | `/api/orders/`                   |

---

## 🛠 Technologies & Knowledge You’ll Need

* **Django REST Framework** – CRUD APIs
* **JWT or Token Auth** – For login/session
* **Signals** – To auto-create profile/cart
* **Stripe SDK** (or similar) – Payment handling
* **Serializer relationships** – nested, `ManyToMany`, etc.
* **Permissions** – User vs Admin actions
* **Custom Actions** – e.g., `@action(detail=True)` in DRF for things like `checkout`, `pay`, etc.

---

Want help visualizing the **ER diagram** or sprint structure next?
