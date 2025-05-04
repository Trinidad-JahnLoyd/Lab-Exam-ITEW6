<template>
    <div>
      <h2>Your Cart</h2>
      <div v-if="cart.length > 0">
        <table class="table">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(item, index) in cart" :key="index">
              <td>{{ item.name }}</td>
              <td>₱{{ item.price }}</td>
              <td><button class="btn btn-danger btn-sm" @click="removeItem(index)">Remove</button></td>
            </tr>
          </tbody>
        </table>
        <div class="text-end">
          <h4>Total: ₱{{ total }}</h4>
          <router-link to="/checkout" class="btn btn-success">Proceed to Checkout</router-link>
        </div>
      </div>
      <div v-else>
        <p>Your cart is empty.</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ShoppingCart',
    data() {
      return {
        cart: [] // Start with an empty cart
      };
    },
    computed: {
      total() {
        return this.cart.reduce((sum, item) => sum + item.price, 0);
      }
    },
    methods: {
      removeItem(index) {
        this.cart.splice(index, 1);
      }
    }
  };
  </script>
  
  
  <style scoped>
  table {
    background-color: white;
  }
  </style>