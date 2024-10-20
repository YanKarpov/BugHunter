--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

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
-- Name: bug_reports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bug_reports (
    id integer NOT NULL,
    category_id integer,
    description text NOT NULL
);


ALTER TABLE public.bug_reports OWNER TO postgres;

--
-- Name: bug_reports_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bug_reports_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.bug_reports_id_seq OWNER TO postgres;

--
-- Name: bug_reports_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bug_reports_id_seq OWNED BY public.bug_reports.id;


--
-- Name: problem_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.problem_categories (
    id integer NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.problem_categories OWNER TO postgres;

--
-- Name: problem_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.problem_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.problem_categories_id_seq OWNER TO postgres;

--
-- Name: problem_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.problem_categories_id_seq OWNED BY public.problem_categories.id;


--
-- Name: bug_reports id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bug_reports ALTER COLUMN id SET DEFAULT nextval('public.bug_reports_id_seq'::regclass);


--
-- Name: problem_categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problem_categories ALTER COLUMN id SET DEFAULT nextval('public.problem_categories_id_seq'::regclass);


--
-- Data for Name: bug_reports; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.bug_reports (id, category_id, description) FROM stdin;
1	1	test
2	2	test2
3	4	test4
4	3	test3
5	2	test5
6	3	test6
7	3	test7
8	1	test8
9	1	test8
10	1	fsd
11	1	test
12	1	test255
13	2	test2556
14	1	test1
15	1	213
16	1	test0
17	1	5325
18	2	test
19	1	test
\.


--
-- Data for Name: problem_categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.problem_categories (id, name) FROM stdin;
1	╨М╥Р ┬о╨▓╨Д╨░╨╗╤Ю┬а╥Р╨▓╨▒╨┐
2	╤Т┬а╨О┬о╨▓┬а╥Р╨▓ ┬н╥Р╨Д┬о╨░╨░╥Р╨Д╨▓┬н┬о
3	тАШ┬л┬о┬м┬а┬л┬а╨▒╨╝ ╤Ю╥Р╨░╨▒╨▓╨Д┬а
4	тАЪ┬о┬з┬м┬о┬ж┬н┬о, ╨│╨┐┬з╤Ю╨Б┬м┬о╨▒╨▓╨╝
\.


--
-- Name: bug_reports_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bug_reports_id_seq', 19, true);


--
-- Name: problem_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.problem_categories_id_seq', 1, false);


--
-- Name: bug_reports bug_reports_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bug_reports
    ADD CONSTRAINT bug_reports_pkey PRIMARY KEY (id);


--
-- Name: problem_categories problem_categories_name_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problem_categories
    ADD CONSTRAINT problem_categories_name_key UNIQUE (name);


--
-- Name: problem_categories problem_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.problem_categories
    ADD CONSTRAINT problem_categories_pkey PRIMARY KEY (id);


--
-- Name: bug_reports bug_reports_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bug_reports
    ADD CONSTRAINT bug_reports_category_id_fkey FOREIGN KEY (category_id) REFERENCES public.problem_categories(id);


--
-- PostgreSQL database dump complete
--

