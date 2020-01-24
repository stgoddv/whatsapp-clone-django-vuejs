<template>
  <div class="contact-profile">
    <!-- Right Sidenavs -->
    <div
      class="absolute user-profile-sidenav right-0 bg-gray-200"
      :style="
        `height: 100%; width: ${Math.min(400, width)}px; z-index:10; 
            transform: translate(${rightSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
      "
    >
      <div class="w-full">
        <div
          class="flex justify-between items-center px-5 bg-teal-500"
          style="height: 10vh;"
        >
          <!-- Close Button -->
          <button
            aria-label="close"
            class="text-xl text-white closebtn"
            @click.prevent="$emit('toggleRightSidenav')"
          >
            ×
          </button>

          <!-- Header -->
          <div class="flex-grow">
            <p class="text-white text-center text-xl">Contact Details</p>
          </div>
        </div>

        <!-- User Details -->
        <div class="user-details">
          <div class="bg-white shadow py-8">
            <!-- Avatar -->
            <div
              class="avatar-main-circle flex-none mx-auto 
                  select-none cursor-pointer hover:shadow-md"
              :style="
                `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); 
          transition: box-shadow 0.3s;`
              "
            >
              {{ getAvatarName }}
            </div>

            <!-- Username -->
            <div class="text-center mt-3">
              <p class="text-lg">{{ getUsername }}</p>
            </div>
          </div>

          <!-- Description -->
          <form class="bg-white shadow py-3 px-6 mt-3">
            <p class="text-left text-sm text-teal-500">Description</p>
            <div class="flex items-center py-2">
              <p class="cursor-default">{{ getUserTagline }}</p>
            </div>
          </form>

          <!-- Delete user -->
          <div
            class="bg-white shadow py-5 px-6 mt-3 
              select-none cursor-pointer hover:bg-gray-200"
            @click="deleteChat"
          >
            <div class="text-left flex items-center">
              <i class="material-icons text-red-600" style="font-size: 28px;"
                >delete</i
              >
              <p class="text-red-600 text-lg mx-3">Delete chat</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  props: ["rightSidenav"],
  methods: {
    deleteChat() {
      const roomId = this.getRoom.id;
      this.$store.commit("SET_SELECTED_ROOM", null);
      this.$store.dispatch("deleteRoom", roomId);
      this.$emit("toggleRightSidenav");
    }
  },
  computed: {
    width() {
      return this.$store.state.width;
    },
    getRoom() {
      let roomId = this.$store.state.selectedRoom;
      return this.$store.state.rooms[roomId] || {};
    },
    getGroupProfile() {
      return this.getRoom.group_profile || {};
    },
    getAvatarName() {
      return this.getGroupProfile.username
        ? this.getGroupProfile.username.charAt(0).toUpperCase()
        : "";
    },
    getUsername() {
      return this.getGroupProfile ? this.getGroupProfile.username : "";
    },
    getUserTagline() {
      return this.getGroupProfile ? this.getGroupProfile.tagline : "";
    },
    getColor() {
      let username = this.getGroupProfile.username || "";
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
  }
};
</script>

<style scoped>
.closebtn {
  font-size: 36px;
}

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
</style>
