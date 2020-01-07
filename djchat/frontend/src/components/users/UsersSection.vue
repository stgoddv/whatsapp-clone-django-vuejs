<template>
  <div
    class="shadow-md border rounded-lg bg-white"
    style=""
  >
    <search class="mt-3" />
    <!-- Lista de usuarios -->
    <div
      class="scrollbar overflow-y-auto user-list mt-3 px-3 pt-1 border"
      style="height: 15rem;"
    >
      <transition-group>
        <div
          v-for="room in rooms"
          :key="room.id"
          @click="selectRoom(room.id)"
          class="user-row"
        >
          <user
            :room="room"
            :isSelected="room.id === $store.state.selectedRoom"
          />
        </div>
      </transition-group>
    </div>
  </div>
</template>

<script>
import User from "./User.vue";
import Search from "@/components/Search.vue";

export default {
  data() {
    return {
      users: []
    };
  },
  components: {
    User,
    Search
  },
  methods: {
    selectRoom(roomId) {
      this.$store.commit("SET_SELECTED_ROOM", roomId);
    }
  },
  computed: {
    rooms() {
      let sortedRooms = Object.values(this.$store.state.rooms).sort((a, b) => {
        return new Date(b.last_activity) - new Date(a.last_activity);
      });
      return sortedRooms;
    }
  }
};
</script>

<style scoped>
.user-row {
  transition: all 0.5s;
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
