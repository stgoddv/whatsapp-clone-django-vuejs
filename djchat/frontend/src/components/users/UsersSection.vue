<template>
  <div
    class="shadow-md border rounded-lg bg-white"
    style=""
  >
    <search class="mt-3" />
    <!-- Lista de usuarios -->
    <div
      class="scrollbar overflow-y-auto user-list mt-3 px-3 pt-1 border"
      style="height: 30rem;"
    >
      <user />
      <user />
      <user isSelected />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
      <user />
    </div>

  </div>
</template>

<script>
import User from "./User.vue";
import Search from "@/components/Search.vue";

export default {
  components: {
    User,
    Search
  }
};
</script>

<style scoped>
/* Scrollbar */
/* width */
.scrollbar::-webkit-scrollbar {
  width: 5px;
}

/* Track */
.scrollbar::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
.scrollbar::-webkit-scrollbar-thumb {
  background: #888;
}

/* Handle on hover */
.scrollbar::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>