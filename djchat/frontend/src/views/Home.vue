<template>
  <div class="home overflow-hidden">
    <!-- Invisible components -->
    <div
      @click="
        leftSidenav = rightSidenav = false;
        toggleOverlay(false);
      "
      id="overlay"
    ></div>
    <invitation-modal ref="invitation-modal" />

    <div class="flex flex-wrap">
      <div class="w-full md:w-1/3">
        <div class="relative bg-white h-screen">
          <!-- Left sidenav -->
          <user-profile
            :leftSidenav="leftSidenav"
            @toggleLeftSidenav="toggleLeftSidenav"
          />

          <SideRooms
            v-if="width < 768"
            ref="mobile-rooms"
            :rightSidenav="rightSidenav"
            :whosWriting="whosWriting"
            @toggleLeftSidenav="toggleLeftSidenav"
            @toggleRightSidenav="toggleRightSidenav"
          />

          <!-- Seccion conversaciones  -->
          <users-section
            class="border-b"
            @profile="toggleLeftSidenav"
            @whosWriting="setWriting($event)"
            @invite-action="openInvitationModal"
            @selected-room="openMobileRooms"
          />

          <!-- Seccion Invitaciones -->
          <invitations @invite-action="openInvitationModal" />
        </div>
      </div>

      <div v-if="width >= 768" class="w-2/3">
        <rooms
          :rightSidenav="rightSidenav"
          :whosWriting="whosWriting"
          @toggleRightSidenav="toggleRightSidenav"
        />
      </div>
    </div>
  </div>
</template>

<script>
import UsersSection from "@/components/users/UsersSection.vue";
import Invitations from "@/components/invitations/Invitations.vue";
import InvitationModal from "@/components/invitations/InvitationModal.vue";
import UserProfile from "@/components/profiles/UserProfile.vue";
import Rooms from "@/components/rooms/Rooms.vue";
import SideRooms from "@/components/rooms/SideRooms.vue";

export default {
  components: {
    UsersSection,
    Invitations,
    InvitationModal,
    UserProfile,
    Rooms,
    SideRooms
  },
  data() {
    return {
      whosWriting: "",
      leftSidenav: false,
      rightSidenav: false
    };
  },
  computed: {
    width() {
      return this.$store.state.width;
    },
    selectedRoom() {
      return this.$store.state.selectedRoom;
    }
  },
  watch: {
    selectedRoom() {
      this.whosWriting = "";
    }
  },
  methods: {
    openInvitationModal() {
      this.$refs["invitation-modal"].open();
    },
    openMobileRooms() {
      if ("mobile-rooms" in this.$refs && this.$refs["mobile-rooms"]) {
        this.$refs["mobile-rooms"].open();
      }
    },
    setWriting(data) {
      const { value, room } = data;
      if (this.selectedRoom === room) {
        this.whosWriting = value;
      }
    },
    toggleOverlay(show) {
      if (show) {
        document.getElementById("overlay").style.display = "block";
      } else {
        document.getElementById("overlay").style.display = "none";
      }
    },
    toggleLeftSidenav() {
      this.leftSidenav = !this.leftSidenav;
      this.toggleOverlay(this.leftSidenav);
    },
    toggleRightSidenav() {
      this.rightSidenav = !this.rightSidenav;
      this.toggleOverlay(this.rightSidenav);
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

#overlay {
  position: fixed; /* Sit on top of the page content */
  display: none; /* Hidden by default */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
}
</style>
