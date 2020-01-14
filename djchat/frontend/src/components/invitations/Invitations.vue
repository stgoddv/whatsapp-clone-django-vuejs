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
            Sent
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
            Received
          </button>
        </nav>
      </div>

      <!-- Tabs Content -->
      <div class="tabs-content">
        <!-- Sent Tab -->
        <div v-if="selectedTab === 0">
          <div
            v-if="Object.entries(sentInvitations).length !== 0"
            class="sent-list"
          >
            <div v-for="invitation in sentInvitations" :key="invitation.id">
              {{ invitation.to_user.name }}
              <user-invitation
                :invitation="invitation"
                :user="invitation.to_user"
                @remove="cancelInvitation"
              />
            </div>
          </div>

          <div v-else class="sent-list empty">
            <p class="text-sm mt-8">Say hello to a friend!</p>

            <invite-button
              class="absolute"
              style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
              @action="showModal = true"
            />
          </div>
        </div>

        <!-- Received Tab -->
        <div v-if="selectedTab === 1">
          <div v-if="receivedInvitations.length !== 0" class="sent-list">
            <div v-for="invitation in receivedInvitations" :key="invitation.id">
              {{ invitation.from_user.name }}
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
            <p class="text-sm mt-8">You have not received any invitation yet</p>

            <invite-button
              class="absolute"
              style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
              @action="showModal = true"
            />
          </div>
        </div>
      </div>
    </div>

    <card-modal :showing="showModal" @close="showModal = false">
      <div class="modal-header">
        <h2 class="text-xl font-bold text-gray-900">Add a Friend!</h2>
        <p class="mt-3">
          Enter his / her email and wait for their answer.
        </p>
      </div>

      <div class="modal-body mt-3">
        <div class="max-w-xs mx-auto">
          <div class="mb-4">
            <input
              class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              id="email"
              type="email"
              placeholder="email"
              v-model="friendEmail"
            />
          </div>
          <p v-if="error" class="text-sm text-red-500">* {{ error }}</p>
        </div>
      </div>

      <div class="action-buttons mt-6">
        <button
          class="mx-3 bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
          @click="addFriend"
        >
          Send
        </button>

        <button
          class="mx-3 bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
          @click="showModal = false"
        >
          Close
        </button>
      </div>
    </card-modal>
  </div>
</template>

<script>
import InviteButton from "./InviteButton";
import UserInvitation from "./UserInvitation";

import CardModal from "@/components/Modal.vue";

export default {
  data() {
    return {
      selectedTab: 0,
      showModal: false,
      friendEmail: "",
      error: ""
    };
  },
  components: {
    CardModal,
    InviteButton,
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
    },
    async addFriend() {
      let userId = null;
      try {
        let response = await this.$store.dispatch(
          "getUserIdFromEmail",
          this.friendEmail
        );
        userId = response.data.id;
      } catch (error) {
        if (error.response.status === 404) {
          this.error = "User not found.";
        } else {
          this.error = "An error has occurred. Please try again later.";
        }
        return;
      }
      try {
        await this.$store.dispatch("addFriend", userId);
        this.showModal = false;
      } catch (error) {
        if (error.response.status === 400) {
          this.error = "You have already sent an invitation.";
        } else {
          this.error = "An error has occurred. Please try again later.";
        }
        return;
      }
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
