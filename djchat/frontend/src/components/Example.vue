<template>
  <div>
    <!-- <div>
            <p>Modal</p>
            <button
              class="bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
              @click="showModal = true"
            >
              Show Modal
            </button>
          </div> -->

    <!-- <card-modal
        :showing="showModal"
        @close="showModal = false"
      >
        <h2 class="text-xl font-bold text-gray-900">Example modal</h2>
        <p class="mb-6">
          This is example text passed through to the modal via a slot.
        </p>
        <button
          class="bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
          @click="showModal = false"
        >
          Close
        </button>
      </card-modal> -->
  </div>
</template>

<script>
// import CardModal from "@/components/Modal.vue";

export default {
  data() {
    return {
      // showModal: false
    };
  },
  components: {
    // CardModal
  }
};
</script>
