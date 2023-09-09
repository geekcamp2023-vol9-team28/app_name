import getLayout from "@/components/layouts/main";
import LoginRequired from "@/components/utils/LoginRequired";
import NotificationList from "@/components/layouts/main/Notification/NotificationList";
import NotificationIcon from "@/components/layouts/main/Notification/NotificationIcon";

const Notification = () => (
  <>
    <LoginRequired />
    <NotificationIcon />
    <NotificationList />
  </>
);

Notification.getLayout = getLayout;

export default Notification;
