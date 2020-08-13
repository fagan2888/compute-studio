import axios from "axios";
import { AccessStatus, Project } from "../types";

export default class API {
  owner?: string;
  title?: string;
  constructor(owner, title) {
    this.owner = owner;
    this.title = title;
  }
  async getAccessStatus(): Promise<AccessStatus> {
    if (this.owner && this.title) {
      return (await axios.get(`/users/status/${this.owner}/${this.title}/`)).data;
    } else {
      return (await axios.get(`/users/status/`)).data;
    }
  }

  async getProject(): Promise<Project> {
    return (await axios.get(`/publish/api/${this.owner}/${this.title}/detail/`)).data;
  }

  async updateProject(data): Promise<Project> {
    return (await axios.put(`/publish/api/${this.owner}/${this.title}/detail/`, data)).data;
  }

  async createProject(data): Promise<Project> {
    return (await axios.post(`/publish/api/`, data)).data;
  }

  async save(data): Promise<Project> {
    if (this.owner && this.title) {
      return await this.updateProject(data);
    } else {
      return await this.createProject(data);
    }
  }
}
