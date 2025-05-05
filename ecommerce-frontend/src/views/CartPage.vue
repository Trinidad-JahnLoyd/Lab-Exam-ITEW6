<template>
    <div class="container mt-4">
      <NavBar />
      <h2>Your Cart</h2>
      <ul class="list-group">
        <li class="list-group-item" v-for="item in cartItems" :key="item.id">
          {{ item.product.name }} - Quantity: {{ item.quantity }}
        </li>
      </ul>
      <button class="btn btn-success mt-3" @click="goToCheckout">Proceed to Checkout</button>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue'
  import { useRouter } from 'vue-router'
  import API from '../api/axios'
  import NavBar from '../components/NavBar.vue'
  
  const addToCart = async (product) => {
  try {
    const res = await API.post('carts/', {
      product: product.id,
      quantity: 1
    })
    alert('Added to cart!')
  } catch (err) {
    console.error(err.response?.data || err.message)
    alert('Please log in or check stock.')
  }
}

  const cartItems = ref([])
  const router = useRouter()
  
  onMounted(async () => {
  try {
    const res = await API.get('carts/')
    const cartData = Array.isArray(res.data) ? res.data[0] : res.data
    cartItems.value = cartData.items || []
  } catch (err) {
    console.error('Error loading cart:', err.response?.data || err.message)
    alert('Please log in to view your cart.')
  }
})

const goToCheckout = () => router.push('/checkout')
  </script>