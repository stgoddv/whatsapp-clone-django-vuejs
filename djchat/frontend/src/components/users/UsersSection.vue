<template>
  <div class="bg-white">
    <!-- Search Panel -->
    <div class="flex items-center search-panel border-b" style="height: 9vh">
      <!-- Avatar -->
      <div
        class="avatar-circle flex-none mx-3 select-none cursor-pointer hover:shadow-md"
        :style="
          `background-color: rgb(${getColor.red},${getColor.green},${getColor.blue}); transition: box-shadow 0.3s;`
        "
        @click="$emit('profile')"
      >
        <!-- {{ room.group_name.charAt(0).toUpperCase() }} -->
        A
      </div>

      <div class="flex-grow ">
        <search
          class="max-w-xs mx-auto pr-3"
          @updateSearch="currentSearch = $event"
        />
      </div>
    </div>

    <!-- Lista de usuarios -->
    <div class="scrollbar overflow-y-auto user-list" style="height: 40vh;">
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
    </div>
  </div>
</template>

<script>
import User from "./User.vue";
import Search from "@/components/Search.vue";

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
    Search
  },
  methods: {
    selectRoom(roomId) {
      this.$store.commit("SET_SELECTED_ROOM", roomId);
    },
    getValues(obj) {
      return [obj.group_name];
    },
    checkIfRowInQueriedResults(id) {
      return this.queriedResults.indexOf(id) != -1;
    }
  },
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
