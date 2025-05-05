<template>
    <div class="container mt-4">
      <NavBar />
      <h2>Admin Panel</h2>
      <div>
        <h4>Products</h4>
        <ul class="list-group">
          <li class="list-group-item" v-for="p in products" :key="p.id">{{ p.name }} - ₱{{ p.price }}</li>
        </ul>
      </div>
      <div>
        <h4>Checkout Transactions</h4>
        <ul class="list-group">
          <li class="list-group-item" v-for="c in checkouts" :key="c.id">Order #{{ c.id }} by user #{{ c.customer }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import API from '../api/axios'
  import NavBar from '../components/NavBar.vue'
  
  const products = ref([])
  const checkouts = ref([])
  
  onMounted(async () => {
    const productRes = await API.get('products/')
    products.value = productRes.data
  
    const checkoutRes = await API.get('orders/')
    checkouts.value = checkoutRes.data
  })
  </script>
  