<template>
    <div class="card h-100">
      <img :src="product.image" class="card-img-top" alt="Product Image">
      <div class="card-body">
        <h5 class="card-title">{{ product.name }}</h5>
        <p class="card-text">₱{{ product.price }}</p>
        <button class="btn btn-primary" @click="$emit('addToCart', product)">Add to Cart</button>
      </div>
    </div>
  </template>
  
  <script setup>
  const props = defineProps({
    product: Object
  })
  </script>
  