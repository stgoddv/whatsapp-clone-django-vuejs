<template>
  <div class="invitation-modal">
    <card-modal class="px-3" :showing="showModal" @close="showModal = false">
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
import CardModal from "@/components/Modal.vue";

export default {
  data() {
    return {
      showModal: false,
      friendEmail: "",
      error: ""
    };
  },
  components: {
    CardModal
  },
  methods: {
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
    },
    open() {
      this.showModal = true;
    },
    close() {
      this.showModal = false;
    }
  }
};
</script>
