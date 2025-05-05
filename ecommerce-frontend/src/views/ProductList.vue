<template>
    <div class="container mt-4">
      <NavBar />
      <h2>Product List</h2>
      <div class="row">
        <div class="col-md-4 mb-4" v-for="product in products" :key="product.id">
          <ProductCard :product="product" @addToCart="addToCart" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import API from '../api/axios'
  import NavBar from '../components/NavBar.vue'
  import ProductCard from '../components/ProductCard.vue'

  
  const products = ref([])
  
  const addToCart = async (product) => {
  try {
    await API.post('carts/', {
      product: product.id,
      quantity: 1
    })
    alert('Added to cart!')
  } catch (err) {
    console.error('Add to cart failed:', err.response?.data || err.message)
    alert(err.response?.data?.error || 'Please log in or check stock.')
  }
}

  

  onMounted(async () => {
    const res = await API.get('products/')
    products.value = res.data
  })
  </script>