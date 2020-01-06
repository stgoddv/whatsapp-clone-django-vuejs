<template>
  <div
    v-if="showing"
    class="absolute inset-0 w-full h-screen flex items-center justify-center"
    style="background-color: rgba(0, 0, 0, 0.75); z-index:1;"
  >
    <div class="relative w-full max-w-2xl bg-white shadow-lg rounded-lg p-8">
      <button
        aria-label="close"
        class="absolute top-0 right-0 text-xl text-gray-500 my-2 mx-4"
        @click.prevent="close"
      >
        ×
      </button>
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  props: {
    showing: {
      required: true,
      type: Boolean
    }
  },
  methods: {
    close() {
      this.$emit("close");
    }
  }
};
</script>