<template>
  <div class="bg-white">
    <!-- Search Panel -->
    <div class="flex items-center search-panel border-b" style="height: 10vh">
      <!-- Avatar -->
      <div
        class="avatar-circle flex-none mx-3 select-none cursor-pointer hover:shadow-md"
        :style="
          `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); transition: box-shadow 0.3s;`
        "
        @click="$emit('profile')"
      >
        {{ getAvatarName }}
      </div>

      <div class="flex-grow ">
        <search
          class="max-w-xs mx-auto pr-3"
          @updateSearch="currentSearch = $event"
        />
      </div>

      <Menu v-if="width < 768" />
    </div>

    <!-- Lista de usuarios -->
    <div class="scrollbar overflow-y-auto user-list" style="height: 50vh;">
      <transition-group>
        <div
          v-for="room in rooms"
          :key="room.id"
          @click="selectRoom(room.id)"
          class="user-row"
          v-show="checkIfRowInQueriedResults(room.id)"
        >
          <user
            :room="room"
            :isSelected="room.id === $store.state.selectedRoom"
            @whosWriting="$emit('whosWriting', $event)"
          />
        </div>
      </transition-group>

      <!-- Fallback message -->
      <invite-friend
        class="mt-8"
        v-if="!rooms.length"
        @invite-action="$emit('invite-action')"
      >
        <p>You have not added any friends yet.</p>
        <p>Say hello to a friend!</p>
      </invite-friend>
    </div>
  </div>
</template>

<script>
import Menu from "@/components/Menu.vue";
import User from "./User.vue";
import Search from "@/components/Search.vue";
import InviteFriend from "@/components/invitations/InviteFriend";

import { colorOffsets, getHash } from "@/global/variables.js";

export default {
  data() {
    return {
      users: [],
      currentSearch: ""
    };
  },
  components: {
    User,
    Menu,
    Search,
    InviteFriend
  },
  methods: {
    selectRoom(roomId) {
      this.$store.commit("SET_SELECTED_ROOM", roomId);
      this.$emit("selected-room");
    },
    getValues(obj) {
      return [obj.group_name];
    },
    checkIfRowInQueriedResults(id) {
      return this.queriedResults.indexOf(id) != -1;
    }
  },
  computed: {
    width() {
      return this.$store.state.width;
    },
    getUserProfile() {
      return this.$store.state.userProfile || {};
    },
    getAvatarName() {
      return this.getUserProfile.username
        ? this.getUserProfile.username.charAt(0).toUpperCase()
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
    },
    rooms() {
      let sortedRooms = Object.values(this.$store.state.rooms).sort((a, b) => {
        return new Date(b.last_activity) - new Date(a.last_activity);
      });
      return sortedRooms;
    },
    queriedResults() {
      var _this2 = this;
      let list = this.rooms;
      if (this.currentSearch == "") return list.map(row => row.id);
      let queriedResults = list.filter(row => {
        let value = _this2
          .getValues(row)
          .toString()
          .toLowerCase();
        return value.indexOf(_this2.currentSearch.toLowerCase()) != -1;
      });
      return queriedResults.map(row => row.id);
    }
  }
};
</script>

<style scoped>
.user-row {
  transition: all 0.5s;
}

.avatar-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 25px;
  color: #fff;
  line-height: 40px;
  text-align: center;
  font-weight: 600;
}

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
