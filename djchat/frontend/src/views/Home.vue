<template>
  <div class="home">

    <div class="flex flex-wrap mt-5">

      <div class="w-3/12 p-3">
        <p class="text-2xl my-4">Whatsapp Clone</p>

        <div
          class="shadow-md border rounded-lg"
          style="min-height: 12rem;"
        >
        </div>

        <div
          class="shadow-md border rounded-lg"
          style="min-height: 12rem; margin-top: 1rem;"
        >
        </div>
      </div>

      <div class="w-9/12 p-3">
        <div class="shadow-md border rounded-lg">
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

export default {
  components: {
    SendForm,
    MessagesSection
  }
};
</script>

<style scoped>
.chat {
  background-image: url("~@/assets/imgs/main-bg.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  background-attachment: fixed;
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