<template>
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="mb-4">Register</h2>
        <div class="card p-4 shadow-sm">
          <form @submit.prevent="registerUser">
            <div class="mb-3">
              <label for="username" class="form-label">Username</label>
              <input v-model="username" type="text" class="form-control" id="username" required />
            </div>
  
            <div class="mb-3">
              <label for="email" class="form-label">Email</label>
              <input v-model="email" type="email" class="form-control" id="email" required />
            </div>
  
            <div class="mb-3">
              <label for="password" class="form-label">Password</label>
              <input v-model="password" type="password" class="form-control" id="password" required />
            </div>
  
            <div class="mb-3">
              <label for="confirmPassword" class="form-label">Confirm Password</label>
              <input v-model="confirmPassword" type="password" class="form-control" id="confirmPassword" required />
            </div>
  
            <div class="text-end">
              <button type="submit" class="btn btn-success">Register</button>
            </div>
  
            <p class="text-danger mt-3" v-if="error">{{ error }}</p>
            <p class="text-success mt-3" v-if="success">{{ success }}</p>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'RegisterPanel',
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        error: '',
        success: ''
      }
    },
    methods: {
      async registerUser() {
        this.error = ''
        this.success = ''
  
        if (this.password !== this.confirmPassword) {
          this.error = "Passwords don't match."
          return
        }
  
        try {
          const response = await axios.post('http://127.0.0.1:8000/api/register/', {
            username: this.username,
            email: this.email,
            password: this.password
          })
  
          if (response.data.success) {
            this.success = 'Registration successful! You can now log in.'
            this.username = ''
            this.email = ''
            this.password = ''
            this.confirmPassword = ''
          } else {
            this.error = response.data.error || 'Registration failed.'
          }
        } catch (err) {
          console.error(err)
          this.error = 'Registration failed. Please try again.'
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

