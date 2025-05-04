import { createRouter, createWebHistory } from 'vue-router'

// Import your views/components
import Storefront from './views/StorefrontPanel.vue'
import ShoppingCart from './components/ShoppingCart.vue'
import AdminPanel from './components/AdminPanel.vue'
import Login from './components/LoginPanel.vue'
import Register from './components/RegisterPanel.vue'
import Checkout from './components/CheckoutPanel.vue'
import ProductList from './components/ProductList.vue'
const routes = [
  { path: '/', name: 'Storefront', component: Storefront },
  { path: '/cart', name: 'ShoppingCart', component: ShoppingCart },
  { path: '/admin', name: 'AdminPanel', component: AdminPanel },
  { path: '/login', name: 'Login', component: Login },
  { path: '/register', name: 'Register', component: Register },
  { path: '/checkout', name: 'Checkout', component: Checkout },
  { path: '/productlist', name: 'ProductList', component: ProductList },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
