<template>
  <div class="user-profile">
    <!-- Left Sidenavs -->
    <div
      class="absolute my-profile-sidenav bg-white"
      :style="
        `height: 100%; width: 100%; z-index:10; 
            transform: translate(${show ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
      "
    >
      <div class=" w-full">
        <rooms
          :rightSidenav="rightSidenav"
          :whosWriting="whosWriting"
          @toggleRightSidenav="$emit('toggleRightSidenav')"
        >
          <button
            aria-label="close"
            class="pl-3"
            style="font-size: 18px;"
            @click.prevent="show = false"
          >
            &xlarr;
          </button>
        </rooms>
      </div>
    </div>
  </div>
</template>

<script>
import Rooms from "./Rooms";

export default {
  components: {
    Rooms
  },
  data() {
    return {
      show: false
    };
  },
  props: {
    rightSidenav: {
      type: Boolean,
      required: true
    },
    whosWriting: {
      type: String,
      required: true
    }
  },
  methods: {
    open() {
      this.show = true;
    }
  },
  watch: {
    show: function(value) {
      if (!value) {
        this.$store.commit("SET_SELECTED_ROOM", null);
      }
    }
  }
};
</script>

<style scoped>
.avatar-main-circle {
  width: 180px;
  height: 180px;
  border-radius: 50%;
  font-size: 130px;
  color: #fff;
  line-height: 180px;
  text-align: center;
  font-weight: 600;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
