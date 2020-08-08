// 建立 socket 连接
var socket = io.connect("http://192.168.31.100:5000/chat");

var records = $("#records");

var auto_scroll = true;

// 监听连接事件
socket.on("connect", (data) => {
    console.log("connect:",data)
})

socket.on("reconnect");

// 监听收到信息
socket.on("message", (resp) => {
    receive_message(resp);
    scroll();
})

// 自动滚动到聊天框底部
records.scroll(function(){
    let total_height = document.getElementById("records").scrollHeight;
    let view_height = $(window).height();
    let height_to_top = records.scrollTop();
    // 如果距离底部高度超过 300，将不再自动滚动到底部
    if(total_height-view_height-height_to_top > 300){
        auto_scroll = false;
    }else{
        auto_scroll = true;
    }
});

// 自动滚动到底部方法
function scroll(){
    if(auto_scroll){
        console.log(document.getElementById("records").scrollHeight);
        document.getElementById("records").scrollTo(0,document.getElementById("records").scrollHeight);
    }
}

// 在聊天框内添加一段对话
function receive_message(resp){
    let html = '<div class="record">' +
        '                <div>' +
        '                    <img class="record-avatar" src="'+resp.avatar+'" />' +
        '                </div>' +
        '                <div class="record-info-container">' +
        '                    <div class="record-info">' +
        '                        <div>'+ resp.nickname +'</div>' +
        '                        <div><div class="record-message">' + resp.message+ '</div></div>' +
        '                    </div>' +
        '                </div>' +
        '            </div>';
    records.append(html);
}

// 发送 socket 消息
function send(){
    let nickname = $("#nickname").val();
    let message = $("#message").val();

    let data = {
        "nickname": nickname,
        "message": message
    }

    socket.emit("message", data);
}