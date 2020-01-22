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
// import SuccessAlert from "./SuccessAlert";
import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  components: {
    // SuccessAlert
    Rooms
  },
  data() {
    return {
      tagline: "",
      show: false,
      isPatching: false,
      showSuccess: false
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
    },
    async patchUserProfile() {
      this.isPatching = true;
      try {
        await this.$store.dispatch("patchUserProfile", {
          tagline: this.tagline
        });
        this.showSuccessAlert();
      } catch (error) {
        console.log(error);
      }
      this.isPatching = false;
    },
    showSuccessAlert() {
      this.showSuccess = true;
      setTimeout(() => {
        this.showSuccess = false;
      }, 5000);
    }
  },
  computed: {
    getUserProfile() {
      return this.$store.state.userProfile || {};
    },
    getAvatarName() {
      return this.getUserProfile.username
        ? this.getUserProfile.username.charAt(0).toUpperCase()
        : "";
    },
    getUsername() {
      return this.$store.state.userProfile
        ? this.$store.state.userProfile.username
        : "";
    },
    getUserTagline() {
      return this.$store.state.userProfile
        ? this.$store.state.userProfile.tagline
        : "";
    },
    getColor() {
      let username = this.getUserProfile.username || "";
      let { red, green, blue } = colorOffsets;
      red = (getHash(username) + red) ** 2 % 256;
      green = (getHash(username) + green) ** 2 % 256;
      blue = (getHash(username) + blue) ** 2 % 256;
      return {
        red,
        green,
        blue
      };
    }
  },
  watch: {
    getUserTagline: function(value) {
      this.tagline = value;
    },
    leftSidenav: function(value) {
      if (value) {
        this.tagline = this.getUserTagline;
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
