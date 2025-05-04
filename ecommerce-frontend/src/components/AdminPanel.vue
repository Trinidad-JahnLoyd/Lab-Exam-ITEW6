<template>
    <div>
      <h2>Admin Panel</h2>
      <ProductList />
    </div>
  </template>
  
  <script>
  import ProductList from './ProductList.vue'
  
  export default {
    name: 'AdminPanel',
    components: { ProductList }
  }
  </script>
  