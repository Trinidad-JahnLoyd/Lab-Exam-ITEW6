<template>
    <div class="container mt-4">
      <NavBar />
      <h2>Checkout</h2>
      <button class="btn btn-primary" @click="checkout">Confirm Purchase</button>
      <p class="text-success mt-3" v-if="success">Checkout successful!</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import API from '../api/axios'
  import NavBar from '../components/NavBar.vue'
  
  const success = ref(false)
  
  const checkout = async () => {
    try {
      await API.post('checkout/')
      success.value = true
    } catch {
      alert('Checkout failed.')
    }
  }
  </script>