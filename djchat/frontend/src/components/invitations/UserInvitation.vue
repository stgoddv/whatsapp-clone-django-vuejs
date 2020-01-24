<template>
  <div
    class="user-row border-b px-3 py-3 select-none rounded-lg"
    style="transition: box-shadow 0.3s, background-color 0.3s;"
  >
    <div class="flex items-center">
      <!-- <img
        class="w-10 h-10 rounded-full mr-4 mr-5 ml-2"
        src="@/assets/avatars/jonathan.jpg"
        alt="Avatar of Jonathan Reinink"
      /> -->
      <div
        class="avatar-circle flex-none mr-3"
        style="background-color: rgb(70,70,70);"
      >
        {{ user.username.charAt(0).toUpperCase() }}
      </div>

      <div class="text-sm w-full">
        <!-- Username -->
        <div class="flex justify-between">
          <p class="text-gray-900 text-left">
            {{ user.username }}
          </p>
        </div>

        <!-- Email -->
        <div class="body-section flex items-center">
          <div>
            <p class="text-gray-600 text-md text-left">
              {{ user.email }}
            </p>
          </div>
        </div>
      </div>

      <!-- Cancel request button -->
      <div v-if="received" class="mx-2">
        <i
          class="material-icons p-2 rounded-full shadow hover:shadow-lg
            cursor-pointer hover:shadow hover:bg-green-300 border"
          style="transition: background-color 0.3s, box-shadow 0.3s;"
          @click="$emit('add', invitation.id)"
          >person_add</i
        >
      </div>

      <!-- Cancel request button -->
      <div class="mx-2">
        <i
          class="material-icons p-2 rounded-full shadow hover:shadow-lg
            cursor-pointer hover:shadow hover:bg-red-300 border"
          style="transition: background-color 0.3s, box-shadow 0.3s;"
          @click="$emit('remove', invitation.id)"
          >delete</i
        >
      </div>
    </div>
  </div>
</template>

<script>
import dateFormat from "dateformat";

export default {
  props: {
    invitation: {
      type: Object,
      required: true
    },
    user: {
      type: Object,
      required: true
    },
    received: {
      type: Boolean,
      required: false
    }
  },
  methods: {
    formatDate(date) {
      let formatted_date = dateFormat(new Date(date), "dd - mm - yyyy");
      return formatted_date;
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
  background: #38b2ac;
}

.avatar-circle {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  font-size: 25px;
  color: #fff;
  line-height: 40px;
  text-align: center;
  font-weight: 600;
}
</style>
