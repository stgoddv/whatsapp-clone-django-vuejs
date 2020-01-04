<template>
  <div
    class="user-row border-b px-3 py-3 cursor-pointer rounded-lg hover:shadow hover:bg-green-200"
    style="transition: box-shadow 0.3s, background-color 0.3s;"
    :class="{ 'bg-green-100':isSelected }"
  >
    <div class="flex items-center">
      <img
        class="w-10 h-10 rounded-full mr-4 mr-5 ml-2"
        src="@/assets/avatars/jonathan.jpg"
        alt="Avatar of Jonathan Reinink"
      >
      <div class="text-sm w-full">
        <div class="flex justify-between">
          <p class="text-gray-900 text-left">Jonathan Reinink</p>
          <p class="text-gray-600 text-xs text-left">15:42</p>
        </div>
        <div class="flex justify-between">
          <p class="text-gray-600 text-md text-left">buena cabros eso es lo que está ...</p>
          <p class="circle mx-1">5</p>
        </div>

      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    isSelected: {
      type: Boolean,
      default: false
    }
  }
};
</script>

<style scoped>
.circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 12px;
  color: #fff;
  line-height: 20px;
  text-align: center;
  background: #38b2ac;
}
</style>