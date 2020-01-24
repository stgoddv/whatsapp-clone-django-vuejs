<template>
  <div class="invitations-tabs">
    <div class="bg-white relative" style="height: 40vh;">
      <!-- Selection Tabs -->
      <div class="tabs-selection bg-white">
        <nav class="flex flex-wrap px-1">
          <!-- Sent Tab -->
          <button
            @click="selectedTab = 0"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{
              'text-blue-500 border-b-2 font-medium border-blue-500':
                selectedTab === 0
            }"
          >
            <div class="flex justify-center">
              <p>Sent</p>
              <p
                v-if="Object.keys(sentInvitations).length"
                class="mx-3 circle bg-indigo-500"
              >
                {{ Object.keys(sentInvitations).length }}
              </p>
            </div>
          </button>

          <!-- Received Tab -->
          <button
            @click="selectedTab = 1"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{
              'text-blue-500 border-b-2 font-medium border-blue-500':
                selectedTab === 1
            }"
          >
            <div class="flex justify-center">
              <p>Received</p>
              <p
                v-if="Object.keys(receivedInvitations).length"
                class="mx-3 circle bg-orange-500"
              >
                {{ Object.keys(receivedInvitations).length }}
              </p>
            </div>
          </button>
        </nav>
      </div>

      <!-- Tabs Content -->
      <div class="tabs-content">
        <!-- Sent Tab -->
        <div v-if="selectedTab === 0">
          <div v-if="Object.entries(sentInvitations).length !== 0">
            <div
              class="sent-list scrollbar overflow-y-auto overflow-x-hidden"
              style="max-height: 20vh;"
            >
              <div v-for="invitation in sentInvitations" :key="invitation.id">
                <user-invitation
                  :invitation="invitation"
                  :user="invitation.to_user"
                  @remove="cancelInvitation"
                />
              </div>
            </div>
            <invite-friend @invite-action="$emit('invite-action')" />
          </div>

          <div v-else class="sent-list empty">
            <invite-friend @invite-action="$emit('invite-action')">
              <p class="text-sm mt-8">Say hello to a friend!</p>
            </invite-friend>
          </div>
        </div>

        <!-- Received Tab -->
        <div v-if="selectedTab === 1">
          <div v-if="receivedInvitations.length !== 0" class="sent-list">
            <div v-for="invitation in receivedInvitations" :key="invitation.id">
              <user-invitation
                received
                :invitation="invitation"
                :user="invitation.from_user"
                @add="acceptInvitation"
                @remove="rejectInvitation"
              />
            </div>
          </div>

          <div v-else class="sent-list empty">
            <invite-friend @invite-action="$emit('invite-action')">
              <p class="text-sm mt-8">
                You have not received any invitation yet
              </p>
            </invite-friend>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import UserInvitation from "./UserInvitation";
import InviteFriend from "./InviteFriend";

export default {
  data() {
    return {
      selectedTab: 0
    };
  },
  components: {
    InviteFriend,
    UserInvitation
  },
  methods: {
    acceptInvitation(invitationId) {
      this.$store.dispatch("acceptFriendRequest", invitationId);
    },
    rejectInvitation(invitationId) {
      this.$store.dispatch("rejectFriendRequest", invitationId);
    },
    cancelInvitation(invitationId) {
      this.$store.dispatch("cancelFriendRequest", invitationId);
    }
  },
  computed: {
    sentInvitations() {
      return this.$store.state.sentInvitations;
    },
    receivedInvitations() {
      return Object.values(this.$store.state.receivedInvitations).filter(
        el => !el.rejected
      );
    }
  }
};
</script>

<style scoped>
.circle {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  font-size: 12px;
  color: #fff;
  line-height: 20px;
  text-align: center;
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
