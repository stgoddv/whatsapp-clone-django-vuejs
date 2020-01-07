<template>
  <div class="invitations-tabs">
    <div
      class="shadow-md border rounded-lg bg-white mt-3 relative"
      style="height: 15rem;"
    >

      <!-- Selection Tabs -->
      <div class="tabs-selection bg-white">
        <nav class="flex flex-wrap px-1">
          <button
            @click="selectedTab = 0"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{ 'text-blue-500 border-b-2 font-medium border-blue-500': selectedTab === 0 }"
          >
            Sent
          </button>
          <button
            @click="selectedTab = 1"
            class="w-1/2 text-gray-600 py-3 block hover:text-blue-500 focus:outline-none"
            :class="{ 'text-blue-500 border-b-2 font-medium border-blue-500': selectedTab === 1 }"
          >
            Received
          </button>
        </nav>
      </div>

      <!-- Tabs Content -->
      <div class="tabs-content">

        <!-- Sent Tab -->
        <div v-if="selectedTab === 0">

          <p class="text-sm mt-8">Say hello to a friend!</p>

          <button
            @click="showModal = true"
            class="absolute py-2 px-4 shadow-md no-underline 
          rounded-full bg-blue-500 text-white font-sans font-semibold 
          text-sm border-blue-500 btn-primary hover:text-white 
          hover:bg-blue-400 focus:outline-none 
          active:shadow-none mr-2"
            style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
          >
            Invite a Friend</button>

        </div>

        <!-- Received Tab -->
        <div v-else>
          <p class="text-sm mt-8">You have not received any invitation yet</p>

          <button
            @click="showModal = true"
            class="absolute py-2 px-4 shadow-md no-underline 
          rounded-full bg-blue-500 text-white font-sans font-semibold 
          text-sm border-blue-500 btn-primary hover:text-white 
          hover:bg-blue-400 focus:outline-none 
          active:shadow-none mr-2"
            style="top: 55%; 
            -ms-transform: translateY(-50%); transform: translateY(-50%);
            -ms-transform: translateX(-50%); transform: translateX(-50%);"
          >
            Invite a Friend</button>
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
            >
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
import CardModal from "@/components/Modal.vue";

export default {
  data() {
    return {
      selectedTab: 0,
      showModal: false
    };
  },
  components: {
    CardModal
  }
};
</script>