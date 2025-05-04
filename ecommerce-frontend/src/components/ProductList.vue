<template>
    <div>
      <div class="mb-3 text-end">
        <button class="btn btn-success" @click="fetchProducts">Refresh List</button>
      </div>
  
      <table class="table table-striped">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Price</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>
              <input v-model="product.name" class="form-control" />
            </td>
            <td>
              <input v-model="product.description" class="form-control" />
            </td>
            <td>
              <input v-model.number="product.price" type="number" class="form-control" />
            </td>
            <td>
              <button class="btn btn-primary btn-sm me-2" @click="updateProduct(product)">Save</button>
              <button class="btn btn-danger btn-sm" @click="deleteProduct(product.id)">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
  
      <p v-if="error" class="text-danger">{{ error }}</p>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'ProductList',
    data() {
      return {
        products: [],
        error: ''
      }
    },
    created() {
      this.fetchProducts()
    },
    methods: {
      async fetchProducts() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/api/products/')
          this.products = response.data
        } catch (err) {
          console.error(err)
          this.error = 'Failed to load products.'
        }
      },
      async updateProduct(product) {
        try {
          await axios.put(`http://127.0.0.1:8000/api/products/${product.id}/`, product)
          alert('Product updated!')
        } catch (err) {
          console.error(err)
          alert('Failed to update product.')
        }
      },
      async deleteProduct(id) {
        if (!confirm('Are you sure you want to delete this product?')) return
  
        try {
          await axios.delete(`http://127.0.0.1:8000/api/products/${id}/`)
          this.products = this.products.filter(p => p.id !== id)
          alert('Product deleted!')
        } catch (err) {
          console.error(err)
          alert('Failed to delete product.')
        }
      }
    }
  }
  </script>
  
  <style scoped>
  input {
    max-width: 200px;
  }
  </style>
  