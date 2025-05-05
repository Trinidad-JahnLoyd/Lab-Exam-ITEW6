import { createRouter, createWebHistory } from 'vue-router'
import LogIn from '../views/LogIn.vue'
import RegisterPage from '../views/RegisterPage.vue'
import ProductList from '../views/ProductList.vue'
import CartPage from '../views/CartPage.vue'
import CheckoutPage from '../views/CheckoutPage.vue'
import AdminPanel from '../views/AdminPanel.vue'

const routes = [
  { path: '/', redirect: '/products' },
  { path: '/login', component: LogIn },
  { path: '/register', component: RegisterPage },
  { path: '/products', component: ProductList },
  { path: '/cart', component: CartPage },
  { path: '/checkout', component: CheckoutPage },
  { path: '/admin', component: AdminPanel, meta: { requiresAuth: true, role: 'Employee' } },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access')
  if (to.meta.requiresAuth && !token) return next('/login')
  next()
})

export default router