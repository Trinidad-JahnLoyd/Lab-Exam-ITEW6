<template>
    <div>
      <h2>Checkout</h2>
      <form @submit.prevent="submitOrder">
        <div class="mb-3">
          <label class="form-label">Full Name</label>
          <input v-model="form.name" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Address</label>
          <input v-model="form.address" type="text" class="form-control" required />
        </div>
        <div class="mb-3">
          <label class="form-label">Payment Method</label>
          <select v-model="form.payment" class="form-control" required>
            <option value="">Select Payment</option>
            <option value="cod">Cash on Delivery</option>
            <option value="gcash">GCash</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Place Order</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CheckoutPanel',
    data() {
      return {
        form: {
          name: '',
          address: '',
          payment: ''
        }
      }
    },
    methods: {
      submitOrder() {
        alert(`Thank you, ${this.form.name}! Your order has been placed.`)
        // Reset form and redirect
        this.form = { name: '', address: '', payment: '' }
        this.$router.push('/')
      }
    }
  }
  </script>
  
  <style scoped>
  form {
    max-width: 500px;
    margin: auto;
  }
  </style>