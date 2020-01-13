<template>
  <div class="invitations-tabs">
    <div
      class="shadow-md border rounded-lg bg-white mt-3 relative"
      style="height: 39vh;"
    >
      <!-- Selection Tabs -->
      <div class="tabs-selection bg-white">
        <nav class="flex flex-wrap px-1">
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
            <div
              v-for="invitation in sentInvitations"
              :key="invitation.id"
            >
              {{ invitation.to_user.name }}
              <user-invitation :invitation="invitation" />
            </div>
          </div>

          <div
            v-else
            class="sent-list empty"
          >
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
        <div v-else>
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

    <card-modal
      :showing="showModal"
      @close="showModal = false"
    >
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
            />
          </div>
        </div>
      </div>

      <div class="action-buttons mt-6">
        <button
          class="bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
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
      showModal: false
    };
  },
  components: {
    CardModal,
    InviteButton,
    UserInvitation
  },
  methods: {},
  computed: {
    sentInvitations() {
      return this.$store.state.sentInvitations;
    }
  }
};
</script>
