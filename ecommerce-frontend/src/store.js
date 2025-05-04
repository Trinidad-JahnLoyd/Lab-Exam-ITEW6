// src/store.js
import { createStore } from 'vuex'

export default createStore({
  state: {
    cart: []
  },
  mutations: {
    ADD_TO_CART(state, product) {
      // Check if product already in cart
      const item = state.cart.find(p => p.id === product.id)
      if (item) {
        item.quantity += 1
      } else {
        state.cart.push({ ...product, quantity: 1 })
      }
    },
    REMOVE_FROM_CART(state, productId) {
      state.cart = state.cart.filter(p => p.id !== productId)
    },
    CLEAR_CART(state) {
      state.cart = []
    }
  },
  actions: {
    addProductToCart({ commit }, product) {
      commit('ADD_TO_CART', product)
    },
    removeProductFromCart({ commit }, productId) {
      commit('REMOVE_FROM_CART', productId)
    },
    clearCart({ commit }) {
      commit('CLEAR_CART')
    }
  },
  getters: {
    cartItems(state) {
      return state.cart
    },
    cartTotal(state) {
      return state.cart.reduce((total, item) => total + item.price * item.quantity, 0)
    },
    cartCount(state) {
      return state.cart.reduce((count, item) => count + item.quantity, 0)
    }
  }
})
