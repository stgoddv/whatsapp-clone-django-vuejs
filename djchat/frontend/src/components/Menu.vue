<template>
  <div class="menu">
    <div
      class="cursor-pointer mr-3 dropdown"
      @mouseover="showContext = true"
      @mouseleave="showContext = false"
    >
      <i class="material-icons text-2xl mx-1 dropbtn">more_vert</i>
      <transition name="fade">
        <div class="dropdown-content rounded-lg" v-if="showContext">
          <a href="/accounts/logout/" class="flex rounded-lg">
            <i class="flex-1 material-icons mr-2">exit_to_app</i>
            <p class="flex-1">Logout</p>
          </a>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showContext: false
    };
  }
};
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s;
}
.fade-enter,
.fade-leave-to {
  transform: translateY(10px);
  opacity: 0;
}

/* DROPDOWN */

/* Style The Dropdown Button */
.dropbtn {
  cursor: pointer;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  position: absolute;
  background-color: #e6fffa;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  right: 0;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: #b2f5ea;
}
</style>
