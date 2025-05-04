<template>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="mb-4">Login</h2>
        <div class="card p-4 shadow-sm">
          <form @submit.prevent="loginUser">
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input v-model="username" type="text" class="form-control" id="username" required />
            </div>
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input v-model="password" type="password" class="form-control" id="password" required />
            </div>
  
            <div class="text-end">
              <button type="submit" class="btn btn-primary">Login</button>
            </div>
  
            <p class="text-danger mt-3" v-if="error">{{ error }}</p>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'LoginPanel',
    data() {
      return {
        username: '',
        password: '',
        error: ''
      }
    },
    methods: {
      async loginUser() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/login/', {
            username: this.username,
            password: this.password
          })
  
          if (response.data.success) {
            alert('Login successful!')
            // Save user session (e.g., localStorage or Vuex)
            localStorage.setItem('user', JSON.stringify(response.data.user))
            this.$router.push('/')
          } else {
            this.error = 'Invalid credentials'
          }
        } catch (err) {
          console.error(err)
          this.error = 'Login failed. Please try again.'
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    background-color: #fff;
  }
  </style>
  