--
-- PostgreSQL database dump
--

\restrict hOMhyXbSa8rJCGqQtfZMB4qlZVVpxM5ucmQmbuHJnJDtqTDeapI2T2CmbPLGDbz

-- Dumped from database version 16.10 (Debian 16.10-1.pgdg13+1)
-- Dumped by pg_dump version 16.10 (Debian 16.10-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: issues; Type: TABLE; Schema: public; Owner: cc_rca_user
--

CREATE TABLE public.issues (
    id integer NOT NULL,
    issue_date date NOT NULL,
    issue_description text NOT NULL,
    solution text,
    root_cause text,
    activity_type character varying(100),
    category character varying(100),
    action_items text,
    status character varying(50),
    added_by character varying(100),
    created_at timestamp without time zone
);


ALTER TABLE public.issues OWNER TO cc_rca_user;

--
-- Name: issues_id_seq; Type: SEQUENCE; Schema: public; Owner: cc_rca_user
--

CREATE SEQUENCE public.issues_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.issues_id_seq OWNER TO cc_rca_user;

--
-- Name: issues_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: cc_rca_user
--

ALTER SEQUENCE public.issues_id_seq OWNED BY public.issues.id;


--
-- Name: issues id; Type: DEFAULT; Schema: public; Owner: cc_rca_user
--

ALTER TABLE ONLY public.issues ALTER COLUMN id SET DEFAULT nextval('public.issues_id_seq'::regclass);


--
-- Data for Name: issues; Type: TABLE DATA; Schema: public; Owner: cc_rca_user
--

COPY public.issues (id, issue_date, issue_description, solution, root_cause, activity_type, category, action_items, status, added_by, created_at) FROM stdin;
2	2025-10-15	The gcda file is not getting created.	let see what is happening.	why this is not updated.	Learning	Build	let work hard here.\r\n	Open	wng	2025-10-18 09:20:41.756752
3	2025-10-13	This issue is resolved now.	Need to raise a ticket for further documentation.	I yet to find the root cause analysis.	Deploy	Documentation	I will raise a ticket. 	Closed	vinodh	2025-10-18 09:20:41.756753
4	2025-10-12	This is not our issue.	Developer fixed this.	Documentation is required.	Check	Code	No action items for us	In Progress	mbiswal	2025-10-18 09:20:41.756754
5	2025-10-16	The job failed. not able to find the exact issue	let learn this	let learn.	issues	Documentation	need to have automation.	In Progress	mbiswal	2025-10-18 09:23:45.689513
1	2025-10-16	I am testing this website.	This section is to tell what is the solution or what we can do.	This section is for finding root cause. This is a good option. let see what is happening.	Build	Process	Update the documentation.	Open	mbiswal	2025-10-18 09:20:41.756746
6	2025-10-15	Test Problems.	Test Solutions	Test Root Cause Analysis.	Build	Process	Test Action Items	In Progress	leccee	2025-10-18 09:27:55.523504
\.


--
-- Name: issues_id_seq; Type: SEQUENCE SET; Schema: public; Owner: cc_rca_user
--

SELECT pg_catalog.setval('public.issues_id_seq', 6, true);


--
-- Name: issues issues_pkey; Type: CONSTRAINT; Schema: public; Owner: cc_rca_user
--

ALTER TABLE ONLY public.issues
    ADD CONSTRAINT issues_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

\unrestrict hOMhyXbSa8rJCGqQtfZMB4qlZVVpxM5ucmQmbuHJnJDtqTDeapI2T2CmbPLGDbz

