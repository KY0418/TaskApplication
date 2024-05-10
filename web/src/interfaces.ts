export interface responseData {
    title: string,
    due_date: string,
    id:number,
    done: boolean
}

export interface eventFLG{
    taskAddFlag: boolean,
}

export interface defData {
    title:string,
    status:string,
    popstatus:boolean,
}

export interface taskContentData {
    title: string,
    status: string,
    popupstatus:boolean,
}

export interface Emits {
    (event: "changeTitle",title:string): void;
}


// export interface requestURL {
//     url: string,
// }

// export interface ResponseApi {
//     title:string,
//     due_date: string,
// }