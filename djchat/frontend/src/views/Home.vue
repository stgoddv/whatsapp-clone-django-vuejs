<template>
  <div class="home">
    <div class="flex flex-wrap">
      <div class="w-1/3 p-3">
        <!-- Seccion conversaciones  -->
        <users-section />

        <div
          class="shadow-md border rounded-lg bg-white mt-3"
          style="min-height: 20vh;"
        >
          <p>Modal</p>
          <button
            class="bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
            @click="showModal = true"
          > Show Modal
          </button>

          <card-modal
            :showing="showModal"
            @close="showModal = false"
          >
            <h2 class="text-xl font-bold text-gray-900">Example modal</h2>
            <p class="mb-6">This is example text passed through to the modal via a slot.</p>
            <button
              class="bg-blue-600 text-white px-4 py-2 text-sm uppercase tracking-wide font-bold rounded-lg"
              @click="showModal = false"
            >
              Close
            </button>
          </card-modal>

        </div>
      </div>

      <div class="w-2/3 p-3">
        <div class="shadow-md border rounded-lg bg-white">
          <div class="flex flex-col justify-between mx-8">
            <!-- Seccion de mensajes -->
            <messages-section class="mt-8" />

            <!-- Envio de mensaje -->
            <send-form class="mt-5" />

            <!-- Footer Copyright -->
            <div class="text-right">
              <a
                style="font-size: 9px;"
                href="http://www.freepik.com"
              >Background vector created by kjpargeter - www.freepik.com</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SendForm from "@/components/SendForm.vue";
import MessagesSection from "@/components/messages/MessagesSection.vue";
import UsersSection from "@/components/users/UsersSection.vue";

import CardModal from "@/components/Modal.vue";

export default {
  components: {
    SendForm,
    MessagesSection,
    UsersSection,
    CardModal
  },
  data() {
    return {
      showModal: false
    };
  }
};
</script>
