<template>
  <div class="user-profile">
    <!-- Left Sidenavs -->
    <div
      class="absolute my-profile-sidenav bg-gray-200"
      :style="
        `height: 100%; width: 100%; z-index:10; 
            transform: translate(-${leftSidenav ? 0 : 150}%);
            transition: transform 0.5s ease-out;`
      "
    >
      <div class="relative w-full">
        <!-- Close Button -->
        <button
          aria-label="close"
          class="absolute top-0 right-0 text-xl text-white mx-2 closebtn"
          @click.prevent="$emit('toggleLeftSidenav')"
        >
          ×
        </button>

        <!-- Header -->
        <div class="bg-teal-500" style="height: 10vh;">
          <p class="text-white pt-3 text-left mx-6 text-xl">My Profile</p>
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
              <!-- {{ room.group_name.charAt(0).toUpperCase() }} -->
              A
            </div>

            <!-- Username -->
            <div class="text-center mt-3">
              <p class="text-lg">Admin</p>
            </div>
          </div>

          <!-- Description -->
          <form class="bg-white shadow py-3 px-6 mt-3">
            <p class="text-left text-sm text-teal-500">Description</p>
            <div
              class="flex items-center border-b border-b-2 border-teal-500 py-2"
            >
              <input
                class="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
                type="text"
                placeholder="Add some info."
                aria-label="Description"
              />
              <button
                class="flex-shrink-0 bg-teal-500 hover:bg-teal-700 border-teal-500 hover:border-teal-700 text-sm border-4 text-white py-1 px-2 rounded"
                type="button"
              >
                Save
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  props: ["leftSidenav"],
  computed: {
    getColor() {
      // let username = this.room.group_name;
      let username = "A";
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
  position: absolute;
  top: 0;
  right: 25px;
  font-size: 36px;
  margin-left: 30px;
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
