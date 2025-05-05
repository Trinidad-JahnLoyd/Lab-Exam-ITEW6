<template>
    <div class="container mt-5">
      <h2>Register</h2>
      <form @submit.prevent="register">
        <input v-model="username" placeholder="Username" class="form-control mb-2" />
        <input v-model="password" type="password" placeholder="Password" class="form-control mb-2" />
        <button class="btn btn-success w-100">Register</button>
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
  
  const register = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/auth/users/', {
        username: username.value,
        password: password.value
      })
      router.push('/products')
    } catch (err) {
      error.value = 'Registration failed'
    }
  }
  </script>
  