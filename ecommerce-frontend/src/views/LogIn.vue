<template>
    <div class="container mt-5">
      <h2>Log In</h2>
      <form @submit.prevent="login">
        <input v-model="username" placeholder="Username" class="form-control mb-2" />
        <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" />
        <button class="btn btn-primary w-100">Login</button>
      </form>
      <p class="text-danger mt-2">{{ error }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  
  const username = ref('')
  const password = ref('')
  const error = ref('')
  const router = useRouter()
  
  const login = async () => {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/token/', {
        username: username.value,
        password: password.value,
      })
    localStorage.setItem('access', response.data.access)
    localStorage.setItem('refresh', response.data.refresh)
    router.push('/products')
    } catch (err) {
      error.value = 'Login failed'
    }
  }
  </script>