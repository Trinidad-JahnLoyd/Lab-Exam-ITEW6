<template>
    <div class="home">
      <h1>Welcome to Our E-Commerce Store</h1>
      <p>Browse our amazing products!</p>
      <router-link to="/storefront" class="btn btn-primary">Go to Storefront</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePanel',
  };
  </script>
  
  <style scoped>
  .home {
    text-align: center;
    margin-top: 50px;
  }
  </style>
  