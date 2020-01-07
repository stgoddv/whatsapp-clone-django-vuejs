<template>
  <div class="home">
    <div class="flex flex-wrap">
      <div class="w-1/3 p-3">
        <!-- Seccion conversaciones  -->
        <users-section />

        <!-- Seccion Invitaciones -->
        <invitations />
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
              <a style="font-size: 9px;" href="http://www.freepik.com"
                >Background vector created by kjpargeter - www.freepik.com</a
              >
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
import Invitations from "@/components/invitations/Invitations.vue";

export default {
  components: {
    SendForm,
    MessagesSection,
    UsersSection,
    Invitations
  }
};
</script>
