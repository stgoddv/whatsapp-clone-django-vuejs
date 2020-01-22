<template>
  <div class="invite-friend">
    <div class="text-sm mt-8">
      <slot></slot>
    </div>
    <invite-button @action="$emit('invite-action')" class="mt-5" />
  </div>
</template>

<script>
import InviteButton from "@/components/invitations/InviteButton";

export default {
  props: {},
  components: {
    InviteButton
  }
};
</script>
