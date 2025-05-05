<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">E-Commerce</router-link>
        <div class="d-flex">
          <router-link class="btn btn-outline-primary me-2" to="/products">Store</router-link>
          <router-link class="btn btn-outline-success me-2" to="/cart">Cart</router-link>
          <router-link class="btn btn-outline-secondary me-2" to="/admin">Admin</router-link>
          <router-link class="btn btn-outline-dark" to="/login">Login</router-link>
          <router-link class="btn btn-outline-dark" to="/register">Register</router-link>
        </div>
      </div>
    </nav>
  </template>