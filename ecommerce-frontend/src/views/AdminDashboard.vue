<template>
    <div class="admin-dashboard">
      <h1>Admin Dashboard</h1>
      <p>Manage your products and view transactions.</p>
      <router-link to="/admin/products" class="btn btn-secondary">Manage Products</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AdminDashboard',
  };
  </script>
  
  <style scoped>
  .admin-dashboard {
    text-align: center;
    margin-top: 50px;
  }
  </style>
  