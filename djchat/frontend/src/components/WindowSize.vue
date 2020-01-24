<template>
  <div class="window-size" />
</template>

<script>
export default {
  data() {
    return {
      window: {
        width: 0,
        height: 0
      }
    };
  },
  created() {
    window.addEventListener("resize", this.handleResize);
    this.handleResize();
  },
  destroyed() {
    window.removeEventListener("resize", this.handleResize);
  },
  methods: {
    handleResize() {
      this.window.width = window.innerWidth;
      this.window.height = window.innerHeight;
      this.$emit("width", this.window.width);
      this.$emit("height", this.window.height);
      this.$store.commit("SET_CURRENT_WIDTH", this.window.width);
      this.$store.commit("SET_CURRENT_HEIGHT", this.window.height);
    }
  }
};
</script>
