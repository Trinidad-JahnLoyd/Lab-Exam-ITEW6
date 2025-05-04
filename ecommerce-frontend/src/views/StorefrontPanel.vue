<template>
    <div>
      <h2>Product Catalog</h2>
      <input v-model="searchQuery" class="form-control mb-3" placeholder="Search products..." />
  
      <div class="row">
        <div v-for="product in filteredProducts" :key="product.id" class="col-md-4 mb-4">
          <div class="card h-100">
            <img :src="product.image" class="card-img-top" alt="Product image" height="200" />
            <div class="card-body">
              <h5 class="card-title">{{ product.name }}</h5>
              <p class="card-text">{{ product.description }}</p>
              <p><strong>₱{{ product.price }}</strong></p>
              <button class="btn btn-primary w-100" @click="addToCart(product)">Add to Cart</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import { mapActions } from 'vuex'

export default {
  name: 'StorefrontPanel',
  data() {
    return {
      searchQuery: '',
      products: [
        { id: 1, name: 'Shirt', description: 'Blue cotton shirt', price: 299, image: 'https://via.placeholder.com/200' },
        { id: 2, name: 'Pants', description: 'Slim fit jeans', price: 499, image: 'https://via.placeholder.com/200' },
        { id: 3, name: 'Shoes', description: 'Running shoes', price: 899, image: 'https://via.placeholder.com/200' }
      ]
    }
  },
  computed: {
    filteredProducts() {
      return this.products.filter(p =>
        p.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      )
    }
  },
  methods: {
    ...mapActions(['addProductToCart']),
    addToCart(product) {
      this.addProductToCart(product)
      alert(`${product.name} added to cart.`)
    }
  }
}
</script>

  
  <style scoped>
  .card-img-top {
    object-fit: cover;
  }
  </style>